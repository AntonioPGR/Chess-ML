#include <iostream>
#include <bits/stdc++.h>

using namespace std;

typedef vector<char> Board;

void displayBoard(Board &board, string message = "", string warning = ""){
  string separator(15, '-');
  string midSeparator(11, '-');
  system("cls");
  cout << separator << endl;
  cout << "  TIC TAC TOE  " << endl;
  cout << separator << endl << endl;
  for(int row = 0; row < 3; row++) {
    int i = row * 3;
    char f1 = board[i] == ' ' ? '1' + i : board[i];
    char f2 = board[i + 1] == ' ' ? '1' + i + 1 : board[i + 1];
    char f3 = board[i + 2] == ' ' ? '1' + i + 2 : board[i + 2];
    cout << "   " << f1 << " | " << f2 << " | " << f3 << endl;
    if (row < 2) cout << "  " << midSeparator << endl;
  }
  cout << endl;
  cout << separator << endl;
  if(message != ""){
    cout << message << endl;
    cout << separator << endl;
  }
  if(warning != ""){
    cout << warning << endl;
    cout << separator << endl;
  }
};

// 1 = X, -1 = O, 0 = Draw
int getWinner(Board &board) {
  int lines[8][3] = {
    {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, // Rows
    {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, // Columns
    {0, 4, 8}, {2, 4, 6}             // Diagonals
  };
  for (int i = 0; i < 8; i++) {
    int a = lines[i][0], b = lines[i][1], c = lines[i][2];
    if (board[a] != ' ' && board[a] == board[b] && board[b] == board[c]) {
      return board[a] == 'X' ? 1 : -1;
    }
  }
  return 0; 
}

bool isGameOver(Board &board) {
  if (getWinner(board) != 0) return true;
  for (int i = 0; i < 9; i++) {
    if (board[i] == ' ') return false;
  }
  return true;
}

int minMax(Board &board, bool isXTurn, int depth = 0, int alpha = INT_MIN, int beta = INT_MAX){
  string str(board.begin(), board.end());
  if(isGameOver(board)) {
    int winner = getWinner(board);
    if (winner == 1) return 10 - depth; 
    if (winner == -1) return depth - 10; 
    return 0;
  };
  char turnPiece = isXTurn? 'X' : 'O';
  int bestValue = isXTurn? INT_MIN : INT_MAX;
  for(int i = 0; i < board.size(); i++){
    if(board[i] == ' '){
      board[i] = turnPiece;
      int value = minMax(board, !isXTurn, depth+1, alpha, beta);
      bestValue = isXTurn? max(value, bestValue) : min(value, bestValue);
      board[i] = ' ';
      if(isXTurn) alpha = max(alpha, bestValue);
      else beta = min(beta, bestValue);
      if(beta <= alpha) break;
    }
  }
  return bestValue;
}
int calculateNextMove(Board &board, bool isXTurn){
  int bestScore = isXTurn ? INT_MIN : INT_MAX;
  vector<int> bestIndices;
  for(int i = 0; i < board.size(); i++){
    if(board[i] == ' '){
      board[i] = isXTurn ? 'X' : 'O';
      int score = minMax(board, !isXTurn);
      board[i] = ' ';
      if((isXTurn && score > bestScore) || (!isXTurn && score < bestScore)){
        bestScore = score;
        bestIndices.clear();  
        bestIndices.push_back(i);
      }
      else if(score == bestScore) bestIndices.push_back(i); 
    }
  }
  if(!bestIndices.empty()){
    int randomIdx = rand() % bestIndices.size();
    return bestIndices[randomIdx] + 1;
  }
  return -1;
}

int main(){
  srand(time(0));
  Board board(9, ' ');

  int who_starts = 0;
  bool invalidStartMessage = false;
  while(who_starts != 1 && who_starts != 2){
    displayBoard(
      board, 
      "  Who starts?\n 1 - Computer\n  2 - Player", 
      invalidStartMessage? "INVALID OPTION - CHOSE 1 OR 2" : ""
    );
    cout << "Choose an option: ";
    cin >> who_starts;
    if(who_starts != 1 && who_starts != 2) invalidStartMessage = true;
  }

  bool isXround = true;
  bool isComputerRound = (who_starts == 1);
  bool invalidMoveMessage = false;
  while(!isGameOver(board)){
    displayBoard(
      board,
      isComputerRound? "" : isXround? "Next to play: X" : "Next to play: O",
      invalidMoveMessage? "INVALID MOVE - CHOSE OTHER" : ""
    );
    int square;
    if(isComputerRound){
      square = calculateNextMove(board, isXround);
    } else {
      cout << "Choose an square: ";
      cin >> square;
      if(square <= 0 || square > 9 || board[square-1] != ' '){
        invalidMoveMessage = true;
        continue;
      }
    }
    board[square-1] = isXround? 'X' : 'O';
    isXround = !isXround;
    isComputerRound = !isComputerRound;
    invalidMoveMessage = false;
  }

  int result = getWinner(board);
  string message = "END GAME: ";
  if(result == 1) message += "X WIN";
  else if(result == -1) message += "O WIN";
  else message += "DRAW";
  displayBoard(board, message);

  return 0;
}