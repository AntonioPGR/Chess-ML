#include <iostream>
#include <bits/stdc++.h>

using namespace std;

typedef vector<char> Board;

void displayBoard(Board board){
  for(int j = 0; j < 15; j++) cout << "-";
  cout << endl;
  cout << "  CHECKERS AI  " << endl;
  for(int j = 0; j < 15; j++) cout << "-";
  cout << endl;
  cout << endl;
  for(int i = 0; i < board.size(); i++){
    char figure = board[i] == ' '? i+49 : board[i];
    if(i == 0 || i == 3 || i == 6) cout << "   " << figure << " | ";
    if(i == 1 || i == 4 || i == 7) cout << figure << " | ";
    if(i == 2 || i == 5 || i == 8) cout << figure << " " << endl;
    if(i == 2 || i == 5) {
      cout << "  ";
      for(int j = 0; j < 11; j++) cout << "-";
      cout << endl;
    }
  }
  cout << endl;
};

// 0 = None, 1 = X, 2 = O, 3 = Draw
int getWinner(Board board) {
  int lines[8][3] = {
    {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, // Rows
    {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, // Columns
    {0, 4, 8}, {2, 4, 6}             // Diagonals
  };
  for (int i = 0; i < 8; i++) {
    int a = lines[i][0], b = lines[i][1], c = lines[i][2];
    if (board[a] != ' ' && board[a] == board[b] && board[b] == board[c]) {
      return board[a] == 'X' ? 1 : 2;
    }
  }
  return 0; 
}

bool isGameOver(Board board) {
  if (getWinner(board) != 0) return true;
  for (int i = 0; i < 9; i++) {
    if (board[i] == ' ') return false;
  }
  return true;
}

int main(){
  Board board(9, ' ');
  bool isXround = true;

  while(!isGameOver(board)){
    displayBoard(board);

    cout << "Next to play: " << (isXround? "X" : "O") << endl;
    cout << "Choose a square: "; 
    int n;
    cin >> n;

    board[n-1] = isXround? 'X' : 'O';
    isXround = !isXround; 

    system("cls");
  }

  displayBoard(board);
  int result = getWinner(board);
  cout << "END GAME: ";
  if(result == 1) cout << "X win";
  else if(result == 2) cout << "O win";
  else cout << "Draw";

  return 0;
}