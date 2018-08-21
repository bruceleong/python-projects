import unittest
import cap

class TestCap(unittest.TestCase):
  def test_one_word(self):
    text = 'python'
    result = cap.cap_text(text)
    self.assertEqual(result, 'Python')
  def test_two_word(self):
    text = 'bruce leong'
    result = cap.cap_text(text)
    self.assertEqual(result, 'Bruce Leong')

if __name__ == '__main__':
  unittest.main()
