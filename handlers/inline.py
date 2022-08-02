import hashlib
from pprint import pprint

from aiogram import types, Dispatcher
from youtube_search import YoutubeSearch as wiki


def finder(text):
    results = wiki(text, max_results=10).to_dict()
    return results


pprint(finder("slivki"))



async def inline_wiki_handler(query: types.InlineQuery):
    text = query.query or "echo"
    link = f"https://ru.wikipedia.org/wiki{text}"
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title="Wikipedia: ",
        url=link,
        input_message_content=types.InputMessageContent(
            message_text=link
        )
    )]
    await query.answer(articles, cache_time=60, is_personal=True)


def register_handlers_inline(dp: Dispatcher):
    # dp.register_inline_handler(inline_youtube_handler)
    dp.register_inline_handler(inline_wiki_handler)