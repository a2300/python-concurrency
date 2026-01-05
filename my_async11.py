import aiohttp
import asyncio
import time

HN_API = "https://hacker-news.firebaseio.com/v0"

async def fetch_story(session, story_id):
    async with session.get(f"{HN_API}/item/{story_id}.json") as response:
        return await response.json()

async def fetch_story_strict(session, story_id):
    story = await fetch_story(session, story_id)
    if story is None:
        raise ValueError(f"Story not found: {story_id}")
    return story

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{HN_API}/topstories.json") as response:
            story_ids = await response.json()
        
        ids_to_fetch = story_ids[:4] + [9999999999]  # Adding a non-existent story ID for testing
        try:
            stories = await asyncio.gather(
                *[fetch_story_strict(session, sid) for sid in ids_to_fetch]
            )
            print(f"Got {len(stories)} stories")
        except ValueError as e:
            print(f"ERROR: {e}")        


asyncio.run(main())