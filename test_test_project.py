from testProject import Game
from testProject import Disk
from testProject import Tower


import unittest
from unittest import mock
from unittest.mock import patch
from unittest import TestCase

import io

"""testing code"""
class Test_tower_puzzle(unittest.TestCase):


    def test_disk_size(self):
        test_disk = Disk(15)

        self.assertEqual(test_disk.size(), 15)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_disk_print_statement(self, mock_stdout):
        test_disk = Disk(3)
        test_disk.print()
        assert mock_stdout.getvalue() == '[ 3 ]\n'

    def test_empty_tower(self):
        test_tower = Tower()

        self.assertTrue(test_tower.empty())
    
    def test_tower_top_isEmpty(self):
        test_tower = Tower()

        self.assertIsNone(test_tower.top())
    
    def test_tower_top_has_disk(self):
        test_tower = Tower()
        test_disk1 = Disk(5)
        test_tower.add(test_disk1)

        self.assertEqual(test_tower.top(), test_disk1)

    def test_tower_pop(self):
        test_tower = Tower()
        test_disk = Disk(0)

        sizes = [15, 13, 7]

        for size in sizes:
            test_disk = Disk(size)
            test_tower.add(test_disk)
            
        self.assertEqual(test_tower.pop(), test_disk)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_tower_print_statement(self, mock_stdout):
        test_tower = Tower()
        test_tower.add(Disk(3))
        test_tower.print()

        assert mock_stdout.getvalue() == 'Needle: [3]\n'
    
    def test_game_has_no_winner(self):
        test_game = Game()

        self.assertFalse(test_game.winner())

    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_tower_print_statement(self, mock_stdout):
        test_game = Game()

        test_game.print()

        assert mock_stdout.getvalue() == 'Needle: [15, 13, 11, 9, 7, 5, 3]\nNeedle: []\nNeedle: []\n'

    def test_game_move(self):
        test_game = Game()
        
        self.assertEqual(test_game.moves(), 0)
    
    '''

    
    @patch('testProject.Game.which_disk', return_value="3")
    def test_game_pick_disk(self, input):
        test_game = Game()

    
    def test_game_whick_disk(self):
        
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: '3'

        test_game = Game()
        input_disk = test_game.which_disk()
        self.assertEqual(input_disk, 3)

        mock.builtins.input = original_input

    '''
    @patch('builtins.input', lambda _: '3')
    def test_game_whick_disk(self):
        
        test_game = Game()

        input_disk = test_game.which_disk()
        assert input_disk == 3
    

    def test_game_pick_disk_is_below_another_one(self):
        
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: '15'

        test_game = Game()
        disk_chosen = test_game.pick_disk()

        self.assertIsNone(disk_chosen)

        mock.builtins.input = original_input


    def test_game_pick_disk_is_valid(self):
    
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: '3'

        test_game = Game()
        disk_chosen = test_game.pick_disk()

        self.assertIsNotNone(disk_chosen)

        mock.builtins.input = original_input

    def test_game_which_tower_invalid_option(self):

        original_input = mock.builtins.input
        mock.builtins.input = lambda _: '24'

        test_game = Game()
        input_tower = test_game.which_tower()

        self.assertIsNone(input_tower)
    
        mock.builtins.input = original_input


    def test_game_which_tower_valid_option(self):

        original_input = mock.builtins.input
        mock.builtins.input = lambda _: '1'

        test_game = Game()
        input_tower = test_game.which_tower()

        self.assertIsNotNone(input_tower)
    
        mock.builtins.input = original_input

    
if __name__ == "__main__":
   #main()
   unittest.main()
    