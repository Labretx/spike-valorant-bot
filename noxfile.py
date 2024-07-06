import nox


@nox.session
def ruff(session):
    session.install("-r", "dev-requirements.txt")
    session.install("-r", "requirements.txt")
    session.run("ruff", "check")


@nox.session
def pyright(session):
    session.install("-r", "dev-requirements.txt")
    session.install("-r", "requirements.txt")
    session.run("pyright")
