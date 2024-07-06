import nox


@nox.session
def build(session):
    session.install("-r", "dev-requirements.txt")
    session.install("-r", "requirements.txt")


@nox.session(reuse_venv=True)
def ruff(session):
    session.run("ruff", "check")


@nox.session(reuse_venv=True)
def pyright(session):
    session.run("pyright")
