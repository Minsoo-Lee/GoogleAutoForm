import json
import os
import time
import traceback

from selenium.webdriver.common.by import By
from form.qa_item import QAItem
from utils.answer_type import  AnswerType
from utils.short_inivt_type import ShortInvitType
from web.webdriver import WebDriver

class CacheManager:
    _instance = None
    _initialized = False
    _cache_dir = r"/Users/minsoo/cache"
    _cache_file = os.path.join(_cache_dir, ".cache")

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CacheManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if CacheManager._initialized:
            return  # 이미 초기화된 경우, 바로 리턴

        self.cache_data = {}

        # 폴더 없으면 생성
        if not os.path.exists(self._cache_dir):
            os.makedirs(self._cache_dir, exist_ok=True)

        CacheManager._initialized = True

    def save_data_internal(self, index, data):
        self.cache_data[index] = data

    def download_data_to_external(self):
        # 저장
        with open(self._cache_file, "w", encoding="utf-8") as f:
            json.dump(self.cache_data, f, ensure_ascii=False, indent=4)

    def upload_data_from_external(self):
        # 파일 없으면 건너뛰기
        if not os.path.exists(self._cache_file):
            return  # 아무것도 안 하고 종료

        with open(self._cache_file, "r", encoding="utf-8") as f:
            # 여기서는 덮어쓰기인데, 어떻게 나오는지 확인할 것
            self.cache_data = json.load(f)
            # key를 숫자로 변환 (필요하면)
            # self.cache_data = {int(k): v for k, v in loaded.items()}

    def is_cache_init(self):
        if not os.path.exists(self._cache_file):
            return False
        return True

    def print_cache_data(self):
        print(self.cache_data)

    def get_cache_data(self):
        return self.cache_data
