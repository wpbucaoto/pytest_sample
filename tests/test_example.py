from pylenium.driver import Pylenium


def test_google(py: Pylenium):
    py.visit('https://google.com')
    py.get('[id="W0wltc"]').click()
    py.get('[name="q"]').type('puppy')
    py.get('[name="btnK"]').submit()
    assert py.should().contain_title('puppy')
