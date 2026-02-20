import pytest
from portfolio.factories import PostFactory  

@pytest.fixture
def project_published():
    return PostFactory.create(
        title='pytest with factory',
    )

@pytest.mark.django_db
def test_create_published_project(project_published):
    assert project_published.title == 'pytest with factory'