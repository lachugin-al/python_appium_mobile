import logging
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--app",
        action="store",
        default="android",
        help="Указываем окружение android или ios"
    )


@pytest.fixture(scope="session")
def app(request):
    return request.config.getoption("--app")


@pytest.fixture(scope='session')
def logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    lf = logging.FileHandler(r'market_app.log', mode='w')
    lf.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', '%m/%d/%Y %I:%M:%S %p')
    lf.setFormatter(formatter)
    logger.addHandler(lf)
    return logger
