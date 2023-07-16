<p align="center">
  <img src="https://www.omkar.cloud/images/favicon/prod/favicon-256x256.png" alt="omkar" />
</p>
  <div align="center" style="margin-top: 0;">
  <h1>✨ Solve Captch in Puppeteer using CapSolver ✨</h1>
</div>
<em>
  <h5 align="center">(Programming Language - Python 3)</h5>
</em>
<p align="center">
  <a href="#">
    <img alt="puppeter-captcha-solving-tutorial forks" src="https://img.shields.io/github/forks/omkarcloud/puppeter-captcha-solving-tutorial?style=for-the-badge" />
  </a>
  <a href="#">
    <img alt="Repo stars" src="https://imbg.shields.io/github/stars/omkarcloud/puppeter-captcha-solving-tutorial?style=for-the-badge&color=yellow" />
  </a>
  <a href="#">
    <img alt="puppeter-captcha-solving-tutorial License" src="https://img.shields.io/github/license/omkarcloud/puppeter-captcha-solving-tutorial?color=orange&style=for-the-badge" />
  </a>
  <a href="https://github.com/omkarcloud/puppeter-captcha-solving-tutorial/issues">
    <img alt="issues" src="https://img.shields.io/github/issues/omkarcloud/puppeter-captcha-solving-tutorial?color=purple&style=for-the-badge" />
  </a>
</p>
<p align="center">
  <img src="https://views.whatilearened.today/views/github/omkarcloud/puppeter-captcha-solving-tutorial.svg" width="80px" height="28px" alt="View" />
</p>

---

🌟 Learn How to Solve Captchas in Puppeteer Using CapSolver 🤖

## 🎯 Overview

This is the final code for the tutorial, which demonstrates how to solve captchas in Puppeteer using CapSolver.

By following this tutorial, you will gain the knowledge to effectively solve captchas, along with best practices to increase the chances of successful captcha solving, such as maintaining consistent user agents and IP addresses.

In the tutorial, we will be solving captchas at [recaptcha-demo.appspot.com](https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php) using CapSolver.

![Captcha Form](https://raw.githubusercontent.com/omkarcloud/puppeter-captcha-solving-tutorial/master/images/recaptcha-v2-checkbox.png)

The tutorial is also available as a YouTube video 🎥, which you can access using the following video:

[![Puppeteer Captcha Solving Tutorial](https://raw.githubusercontent.com/omkarcloud/puppeter-captcha-solving-tutorial/master/images/video.png)](TODO_YOUTUBE_LINK)

## 🚀 Running the Code
If you are interested in seeing the captcha-solving process in action, follow these steps:

1️⃣ Clone the repository 🧙‍♀️:
```shell
git clone https://github.com/omkarcloud/puppeter-captcha-solving-tutorial
cd puppeter-captcha-solving-tutorial
```

2️⃣ Install Dependencies 📦:
```shell
python -m pip install pyppeteer capsolver-python
```

3️⃣ Get your CapSolver API Key by following the "Setup CapSolver" section of this tutorial. You can view the section [here](TODO).

![Store API Key](https://raw.githubusercontent.com/omkarcloud/puppeter-captcha-solving-tutorial/master/images/store-api-key.png)

4️⃣ In `main.py`, replace `YOUR_API_KEY` with your CapSolver API Key. 🗝️

5️⃣ Run the code to solve the captcha. 🏃‍♀️

```shell
python main.py
```

Once the captcha is successfully solved, you will be greeted with the following success screen 😎.

![Solved Captcha Success Page](https://raw.githubusercontent.com/omkarcloud/puppeter-captcha-solving-tutorial/master/images/solved-captcha-success-page.png)

## ✅ Final Code

This is the final code of `main.py` that solves the captcha. I encourage you to read and understand the code to grasp the process of captcha solving.

```python
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
```

---

## Love It? Star It! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=omkarcloud/puppeter-captcha-solving-tutorial&type=Timeline)](https://star-history.com/#omkarcloud/puppeter-captcha-solving-tutorial&Timeline)


<!-- TOSO:
    Article /blog/ replacement
    TODO: VIDEO FIX
 -->