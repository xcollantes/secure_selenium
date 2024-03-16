# Secure Selenium Python Template

Secure Selenium driver with settings.

## Usage

1. `my_instance = SecureSelenium(<webdriver path>, <user agent>, <if headless
display>)`
1. `my_instance.get(<url>)`

## Example

```
user_agent: str = "Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"

my_instance: SecureSelenium = SecureSelenium(
  "path/to/webdriver", user_agent, False)

some_response: str = my_instance.get(<url>)
```

# How to update Chrome and Selenium Chrome webdriver

_IMPORTANT: Chrome browser and Chrome webdriver must match in version but not
necessarily the same version number._

1. Download the Chrome browser

   https://googlechromelabs.github.io/chrome-for-testing/#stable
   
1. Download the matching webdriver
   1. https://googlechromelabs.github.io/chrome-for-testing/#stable
   1. Before building, `unzip` zip file and name the binary `chromedriver`.

## Common pitfalls

**Selenium can't find my browser.**

Ensure the location of the Chrome browser is in the environment variable
`$PATH`.

**Never specify the `--noheadless` flag for Docker.**

This will result in `(unknown error: DevToolsActivePort file doesn't exist) (The
  process started from chrome location /usr/bin/google-chrome is no longer
  running, so ChromeDriver is assuming that Chrome has crashed.)`
