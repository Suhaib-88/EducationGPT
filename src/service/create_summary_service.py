from utils.summary_writer import SummaryWriter
from utils.cache_handler import CacheHandler
import gradio as gr

def create_summary(link, p_input):
    if CacheHandler().judge_subtitle_cache() is None:
        summary= SummaryWriter(yt_info),write_summary()
        return [gr.update(value= yt_subtitle), gr.update(value= summary)]
    else:
        yt_info_cache= CacheHandler().judge_subtitle_cache(y_cid)
        yt_subtitle= yt_info_cache['subtitle']
        return [gr.update(value= yt_subtitle), gr.update(value= summary)]
 