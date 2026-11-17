import time, sys
sys.path.insert(0, '.')
import engine as E
# Semi-Slav position after 8 moves (game 1, slow)
fen = "rnbqkbnr/pp3ppp/2p1pn2/3p4/2PP4/2N1PN2/PP3PPP/R1BQKB1R w KQkq - 0 5"
E.load(fen)
# time a 60k-node search
E.LM = 60000
E.ND = 0
t0 = time.time()
try:
    best = E.pick(fen, [], 60000, "bench")
except Exception as ex:
    print("exc", ex)
t1 = time.time()
print(f"pick nodes={E.ND} time={t1-t0:.2f}s nps={E.ND/max(t1-t0,0.01):.0f} best={best}")
# middlegame position (open)
fen2 = "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3"
E.load(fen2)
E.ND = 0
t0 = time.time()
try:
    best = E.pick(fen2, [], 60000, "bench2")
except Exception as ex:
    print("exc", ex)
t1 = time.time()
print(f"pick2 nodes={E.ND} time={t1-t0:.2f}s nps={E.ND/max(t1-t0,0.01):.0f} best={best}")
