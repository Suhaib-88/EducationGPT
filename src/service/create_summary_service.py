from src.utils.summary_writer import SummaryWriter
from src.utils.cache_handler import CacheHandler
import gradio as gr
from langchain.document_loaders import YoutubeLoader 
from langchain_community.document_loaders.youtube import TranscriptFormat


def create_summary(link):
    if CacheHandler().judge_subtitle_cache() is None:
        loader = YoutubeLoader.from_youtube_url(link, transcript_format=TranscriptFormat.CHUNKS,add_video_info=False)
        transcript= loader.load()
        summary= SummaryWriter(transcript).write_summary()
        return [gr.update(value= yt_subtitle), gr.update(value= summary)]
    else:
        yt_info_cache= CacheHandler().judge_subtitle_cache(y_cid)
        yt_subtitle= yt_info_cache['subtitle']
        return [gr.update(value= yt_subtitle), gr.update(value= summary)]
 