import java.awt.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class GeniusSquareGame {
    private static final int GRID_SIZE = 6;
    private static final char BLOCKER = '#';
    private static final char EMPTY = '.';
    private static final char[] PIECES = {'R', 'B', 'G', 'Y', 'C', 'M', 'O', 'P', 'A'};
    private static final int[][][] PIECE_SHAPES = {
        {{0, 0}, {0, 1}, {0, 2}, {0, 3}},
        {{0, 0}, {0, 1}, {1, 0}, {1, 1}},
        {{0, 0}, {1, 0}, {2, 0}, {2, 1}},
        {{0, 0}, {1, 0}, {2, 0}, {1, 1}},
        {{0, 0}, {1, 0}, {1, 1}, {2, 1}},
        {{0, 0}, {0, 1}, {0, 2}},
        {{0, 0}, {0, 1}},
        {{0, 0}},
        {{0, 0}, {0, 1}, {1, 0}}
    };

    private char[][] board;
    private List<Point> blockers;
    private List<int[][]> pieces;
    private Random rand;

    public GeniusSquareGame() {
        board = new char[GRID_SIZE][GRID_SIZE];
        blockers = new ArrayList<>();
        pieces = new ArrayList<>();
        rand = new Random();
        clearBoard();
        initializePieces();
    }

    private void clearBoard() {
        for (int i = 0; i < GRID_SIZE; i++) {
            for (int j = 0; j < GRID_SIZE; j++) {
                board[i][j] = EMPTY;
            }
        }
    }

    private void initializePieces() {
        for (int[][] shape : PIECE_SHAPES) {
            pieces.add(shape);
        }
    }

    private void printBoard() {
        for (int i = 0; i < GRID_SIZE; i++) {
            for (int j = 0; j < GRID_SIZE; j++) {
                System.out.print(board[i][j] + "  ");
            }
            System.out.println();
        }
        System.out.println();
    }

    private void placeRandomBlockers() {
        blockers.clear();
        while (blockers.size() < 7) {
            int x = rand.nextInt(GRID_SIZE);
            int y = rand.nextInt(GRID_SIZE);
            Point blocker = new Point(x, y);
            if (!blockers.contains(blocker) && board[x][y] == EMPTY) {
                blockers.add(blocker);
                board[x][y] = BLOCKER;
            }
        }
    }

    private void placeManualBlockers() {
        Scanner scanner = new Scanner(System.in);
        blockers.clear();
        System.out.println("Enter the coordinates");
        while (blockers.size() < 7) {
            System.out.print("Blocker " + (blockers.size() + 1) + ": ");
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            if (x >= 0 && x < GRID_SIZE && y >= 0 && y < GRID_SIZE && board[x][y] == EMPTY) {
                Point blocker = new Point(x, y);
                blockers.add(blocker);
                board[x][y] = BLOCKER;
            } else {
                System.out.println("Invalid or duplicate coordinates. Try again.");
            }
        }
    }

    private boolean canPlacePiece(int[][] piece, int x, int y) {
        for (int[] p : piece) {
            int newX = x + p[0];
            int newY = y + p[1];
            if (newX < 0 || newX >= GRID_SIZE || newY < 0 || newY >= GRID_SIZE || board[newX][newY] != EMPTY) {
                return false;
            }
        }
        return true;
    }

    private void placePiece(int[][] piece, int x, int y, char symbol) {
        for (int[] p : piece) {
            int newX = x + p[0];
            int newY = y + p[1];
            board[newX][newY] = symbol;
        }
    }

    private boolean tryToPlacePiece(int[][] piece, char symbol) {
        for (int i = 0; i < GRID_SIZE; i++) {
            for (int j = 0; j < GRID_SIZE; j++) {
                if (canPlacePiece(piece, i, j)) {
                    placePiece(piece, i, j, symbol);
                    return true;
                }
            }
        }
        return false;
    }

    private boolean rotateAndPlacePiece(int[][] piece, char symbol) {
        for (int rotation = 0; rotation < 4; rotation++) {
            if (tryToPlacePiece(piece, symbol)) {
                return true;
            }
            piece = rotatePiece(piece);
        }
        return false;
    }

    private int[][] rotatePiece(int[][] piece) {
        int[][] rotatedPiece = new int[piece.length][2];
        for (int i = 0; i < piece.length; i++) {
            rotatedPiece[i][0] = -piece[i][1];
            rotatedPiece[i][1] = piece[i][0];
        }
        return rotatedPiece;
    }

    private boolean isBoardFull() {
        for (int i = 0; i < GRID_SIZE; i++) {
            for (int j = 0; j < GRID_SIZE; j++) {
                if (board[i][j] == EMPTY) {
                    return false;
                }
            }
        }
        return true;
    }

    public void autoSolve() {
        boolean allPlaced = false;
        while (!allPlaced) {
            clearBoard();
            placeRandomBlockers();
            allPlaced = true;
            for (int i = 0; i < pieces.size(); i++) {
                char pieceColor = PIECES[i];
                if (!rotateAndPlacePiece(pieces.get(i), pieceColor)) {
                    allPlaced = false;
                    break;
                }
            }
        }
        printBoard();
        
    }

    public static void main(String[] args) {
        GeniusSquareGame game = new GeniusSquareGame();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Choose blocker placement mode:");
        System.out.println("1. Random placement");
        System.out.println("2. Manual placement");
        System.out.print("Enter your choice: ");
        int choice = scanner.nextInt();

        if (choice == 1) {
            game.placeRandomBlockers();
        } else if (choice == 2) {
            game.placeManualBlockers();
        } else {
            System.out.println("Invalid choice. Defaulting to random placement.");
            game.placeRandomBlockers();
        }

        System.out.println("R is a 4-unit horizontal line");
        System.out.println("B is a 2x2 block");
        System.out.println("G is an L-shape");
        System.out.println("Y is a T-shape");
        System.out.println("C is a Z-shape");
        System.out.println("M is a 3-unit horizontal line");
        System.out.println("O is a 2-unit horizontal line");
        System.out.println("P is a 1-unit piece");
        System.out.println("A is a 3x1 vertical block");

        game.autoSolve();
    }
}
