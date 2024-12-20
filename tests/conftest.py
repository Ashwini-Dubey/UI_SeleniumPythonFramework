import pytest
from selenium import webdriver

drive = None

#Adding command line option to specify the browser name
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome"
    )

# Fixture for setting up and tearing down the WebDriver
@pytest.fixture(scope="class")
def setup(request):
    """
    Pytest fixture to initialize and configure the WebDriver.
    It reads the browser name from the command line and sets up the corresponding WebDriver.
    After the test execution, it tears down the WebDriver.
    """

    global driver
    # Get browser name from CLI
    browser_name = request.config.getoption("browser_name")

    if browser_name == 'Chrome':
        driver = webdriver.Chrome()  # setup Chrome WebDriver

    elif browser_name == 'Firefox':
        driver = webdriver.Firefox()  # setup Firefox WebDriver

    elif browser_name == 'Safari':
        driver = webdriver.Safari()  # setup Safari WebDriver

    # Open the target URL
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(10)
    driver.maximize_window()

    request.cls.driver = driver  # attach the driver to the class
    yield
    driver.quit()  # teardown: close the WebDriver after the test completes

#Utility method to attach the screenshot for the failed cases with the HTML report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = (
                    '<div>'
                    '<img src="{0}" alt="screenshot" style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right">'
                    '</div>'
                ).format(file_name)
                extra.append(pytest_html.extras.html(html))
    report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
