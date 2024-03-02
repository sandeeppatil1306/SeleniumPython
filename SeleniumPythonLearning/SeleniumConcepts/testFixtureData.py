import logging

import pytest

from SeleniumConcepts.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):
    def test_editProfile(self,dataLoad):
        log = self.test_loggingDemo()
        log.info(dataLoad[0])
        log.info(dataLoad[1])
        print(dataLoad)
