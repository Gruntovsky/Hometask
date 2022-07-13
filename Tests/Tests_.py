import bookkeeping
from unittest.mock import patch

class Tests_Pytest:

    @classmethod
    def setUp(cls):
        print('method setUp')

    @patch('bookkeeping.input')
    def test_delete_doc(self, mock_input):
        mock_input.return_value = '10006'
        assert bookkeeping.delete_doc() == ('10006', True)

    @patch('bookkeeping.input')
    def test_get_doc_owner_name(self, mock_input):
        mock_input.return_value = '11-2'
        assert bookkeeping.get_doc_owner_name() == ('Геннадий Покемонов')

    @patch('bookkeeping.input')
    def test_move_doc_to_shelf(self, mock_input):
        mock_input.side_effect = [bookkeeping.documents[1]['number'], '3']
        bookkeeping.move_doc_to_shelf()
        assert bookkeeping.directories['3'] == ['11-2']

    def test_show_document_info(self):
        bookkeeping.show_document_info(bookkeeping.documents[0])
        assert bookkeeping.documents[0]['type'] == "passport" \
               and bookkeeping.documents[0]['number'] == '2207 876234'

    @classmethod
    def tearDown(cls):
        print('method tearDown')