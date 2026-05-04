import asyncio
import os
from playwright.async_api import async_playwright

async def run_scraper():
    print("Starting scraper...")

    PROXY_SERVER = os.getenv("PROXY_SERVER", "http://45.196.152.88:63056")
    print(f"Using proxy: {PROXY_SERVER}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            proxy={"server": PROXY_SERVER}
        )
        try:
            context = await browser.new_context()
            page = await context.new_page()

            # Test proxy is working
            print("Testing proxy connection...")
            await page.goto("https://httpbin.org/ip", timeout=60000)
            ip_info = await page.inner_text("body")
            print(f"Running with IP: {ip_info}")

            # --- YOUR SCRAPING LOGIC HERE ---
            # Example: scrape AppStoreSpy channels
            # await page.goto("https://appstorespy.com/...", timeout=60000)
            # channels = await page.query_selector_all(".channel-item")
            # for ch in channels:
            #     name = await ch.inner_text()
            #     print(f"Channel: {name}")

            print("Scraper cycle completed successfully.")

        finally:
            await browser.close()
            print("Browser closed.")

async def main():
    print("Starting CloudBot...")
    while True:
        try:
            await run_scraper()
            print("Cycle done. Waiting 60 seconds...")
            await asyncio.sleep(60)
        except Exception as e:
            print(f"Error: {e} — retrying in 30 seconds...")
            await asyncio.sleep(30)

if __name__ == "__main__":
    asyncio.run(main())
