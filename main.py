import asyncio
from pyppeteer import launch
from capsolver_python import RecaptchaV2Task

# Following code solves a reCAPTCHA v2 challenge using CapSolver.
async def main():
    # Launch Browser.
    browser = await launch({'headless': False})

    # Load the target page.
    captcha_page_url = "https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php"
    page = await browser.newPage()
    await page.goto(captcha_page_url)

    # Solve the reCAPTCHA using CapSolver.
    print("Solving captcha")
    capsolver = RecaptchaV2Task("YOUR_API_KEY")

    site_key = "6LfW6wATAAAAAHLqO2pb8bDBahxlMxNdo9g947u9"
    task_id = capsolver.create_task(captcha_page_url, site_key)
    result = capsolver.join_task_result(task_id)

    # Get the solved reCAPTCHA code.
    code = result.get("gRecaptchaResponse")
    print(f"Successfully solved the reCAPTCHA. The solve code is {code}")

    # Set the solved reCAPTCHA code on the form.
    recaptcha_response_element = await page.querySelector('#g-recaptcha-response')
    await page.evaluate(f'(element) => element.value = "{code}"', recaptcha_response_element)

    # Submit the form.
    submit_btn = await page.querySelector('button[type="submit"]')
    await submit_btn.click()

    # Pause the execution so you can see the screen after submission before closing the driver
    input("Captcha Submission Successfull. Press enter to continue")

    # Close Browser.
    await browser.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
