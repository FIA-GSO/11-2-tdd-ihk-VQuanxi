import pytest
from notenberechnung import berechne_prozentwert, bestimme_note

testdata = [
  (100, "sehr gut"),
  (92,"sehr gut"),
  (92,"gut"),
  (81,"gut"),
  (80,"befriedigend"),
  (67,"befriedigend"),
  (66,"ausreichend"),
  (50,"ausreichend"),
  (49,"mangelhaft"),
  (30,"mangelhaft"),
  (29,"ungenügend"),
  (0,"ungenügend"),
  (-1,"ValueError"),
  (101,"ValueError"),
  ('text',"TypeError"),
]

@pytest.mark.parametrize("value, expected", testdata)
def test_bestimme_note__korrekte_note_wird_berechnet(value, expected):
    # arrange
    erreichter_prozentwert = value
    erwartetes_ergebnis = expected
    
    # act
    ergebnis = bestimme_note(erreichter_prozentwert)
    
    # assert
    assert erwartetes_ergebnis == ergebnis