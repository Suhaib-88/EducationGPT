from langchain.document_loaders import YoutubeLoader
from src.common.config import Config
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.prompts.structured_prompts import SUMMARY_PROMPT
from src.utils.cache_handler import CacheHandler

class SummaryWriter:
    def __init__(self, transcript) -> None:
        self.subtitle = transcript[0].page_content
        self.seg_length = 3000
        self.summary_count = 5 if len(self.subtitle) is None else self.subtitle
        self._llm = Config().get_llm()
        self._summary_chain = Config.create_llm_chain(llm=self._llm, prompt=SUMMARY_PROMPT)
        self._cache_handler = CacheHandler()

        



    def write_summary(self) -> str:
        summary_ans = ""
        pre_summary_text = self._summary_seg_content()
        for chunk in pre_summary_text:
            summary_ans += self._get_summary(chunk)
        if len(pre_summary_text) >= 2:
            summary_ans = self._get_summary(summary_ans)

        self._cache_handler.subtitle_cache(b_cid=self.b_cid,
                                           title=self.title,
                                           subtitle=self.subtitle,
                                           summary=summary_ans)
        return summary_ans

    def _summary_seg_content(self):
        if len(self.subtitle) > self.seg_length:
            r_splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.seg_length,
                chunk_overlap=200
            )
            split_texts = r_splitter.split_text(self.subtitle)
            return split_texts
        else:
            return [self.subtitle]

    def _get_summary(self, chunk) -> str:
        summary_response = self._summary_chain.run(
            summary_count=self.summary_count,
            subtitle=chunk
        )
        return summary_response