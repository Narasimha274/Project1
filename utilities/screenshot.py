from datetime import datetime

def capture(driver):

    # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    driver.save_screenshot(
        f"screenshots1.png"
    )
    #from utilities.screenshot import capture

    try:
        assert "inventory" in driver.current_url
    except:
        capture(driver)
        raise