from typing import Optional, List
from urllib.parse import urlparse

import validators
from pydantic import BaseModel, field_validator, Field

from page_analyzer.services.utils import get_date_now

URL_MAX_LENGTH = 255


class URLBaseMixin(BaseModel):
    id: Optional[int] = None
    created_at: str = Field(default_factory=get_date_now)


class URLModel(BaseModel):
    name: str = Field(max_length=URL_MAX_LENGTH)

    @field_validator('name')
    def validate_url(cls, value: str) -> str:

        if validators.url(value):
            url = urlparse(value)
            return f'{url.scheme}://{url.netloc}'.lower()
        raise ValueError('Некорректный URL')


class URLChecks(URLBaseMixin):
    url_id: int
    status_code: Optional[int] = None
    h1: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None


class URLSModel(URLBaseMixin, URLModel):
    url_checks: Optional[List[URLChecks]] = []