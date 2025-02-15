from .utils import skip_projects_except


@skip_projects_except(["with-dependency"])
def test_get_project_without_contracts_path(project):
    proj_path = project.path / "dependency_c"
    proj = project.get_project(proj_path)
    assert proj.contracts_folder == proj_path / "contracts"


@skip_projects_except(["with-dependency"])
def test_get_project_with_contracts_path(project):
    proj_path = project.path / "dependency_a"
    proj = project.get_project(proj_path, proj_path / "sources")
    assert proj.contracts_folder != proj_path / "contracts"
    assert proj.contracts_folder == proj_path / "sources"
