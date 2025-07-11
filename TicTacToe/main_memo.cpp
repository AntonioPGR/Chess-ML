#include <iostream>
#include <bits/stdc++.h>

using namespace std;

typedef vector<char> Board;

unordered_map<string, int> MEMO;

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

string rotate90(const string &b) {
  return string{b[6], b[3], b[0],b[7], b[4], b[1],b[8], b[5], b[2]};
}
string mirrorH(const string &b) {
  return string{b[6], b[7], b[8],b[3], b[4], b[5],b[0], b[1], b[2]};
}
string mirrorV(const string &b) {
  return string{b[2], b[1], b[0],b[5], b[4], b[3],b[8], b[7], b[6]};
}
void memorizeSymmetries(string board, int winner){
  vector<string> symmetries;
  string r0 = board;
  string r90 = rotate90(r0);
  string r180 = rotate90(r90);
  string r270 = rotate90(r180);
  symmetries.push_back(r0);
  symmetries.push_back(r90);
  symmetries.push_back(r180);
  symmetries.push_back(r270);
  symmetries.push_back(mirrorH(r0));
  symmetries.push_back(mirrorH(r90));
  symmetries.push_back(mirrorH(r180));
  symmetries.push_back(mirrorH(r270));
  for(const string &s : symmetries) {
    MEMO[s] = winner;
  }
}

int minMax(Board &board, bool isXTurn, int alpha = INT_MIN, int beta = INT_MAX){
  string str(board.begin(), board.end());
  if(MEMO.count(str)) return MEMO[str];
  if(isGameOver(board)) {
    int winner = getWinner(board);
    memorizeSymmetries(str, winner);
    return winner;
  };
  char turnPiece = isXTurn? 'X' : 'O';
  int bestValue = isXTurn? INT_MIN : INT_MAX;
  for(int i = 0; i < board.size(); i++){
    if(board[i] == ' '){
      board[i] = turnPiece;
      int value = minMax(board, !isXTurn, alpha, beta);
      bestValue = isXTurn? max(value, bestValue) : min(value, bestValue);
      board[i] = ' ';
      if(isXTurn) alpha = max(alpha, bestValue);
      else beta = min(beta, bestValue);
      if(beta <= alpha) break;
    }
    if((bestValue == 1 && isXTurn) || (bestValue == -1 && !isXTurn)) break;
  }
  return bestValue;
}

int calculateNextMove(Board &board, bool isXTurn){
  int bestScore = isXTurn ? INT_MIN : INT_MAX;
  int bestIndex = -1;
  for(int i = 0; i < board.size(); i++){
    if(board[i] == ' '){
      board[i] = isXTurn? 'X' : 'O';
      int score = minMax(board, !isXTurn);
      board[i] = ' ';
      if((isXTurn && score > bestScore) || (!isXTurn && score < bestScore)){
        bestIndex = i;
        bestScore = score;
      }
    }
  }
  return bestIndex + 1;
}

int main(){
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