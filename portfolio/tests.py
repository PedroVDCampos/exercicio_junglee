import pytest
from portfolio.models import Project

@pytest.mark.django_db
def test_project_model_creation():
    project = Project.objects.create(
        title="Projeto Teste",
        description="Descricao teste",
        technology="Python"
    )
    assert project.title == "Projeto Teste"
    assert Project.objects.count() == 1