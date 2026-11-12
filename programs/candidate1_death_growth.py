"""candidate1_death_growth.py — кандидат №1 пробы пера (линза «рождение и смерть», автор vtora).

Семя: множество HJSW в окне 2p×2p (paper/hjsw_window.tex saturation: G(p) = [-h, 3h+1] × [0, 2p-1], h=(p-1)/2;
гипербола xy ≡ c (mod p); из четырёх копий каждого класса вычитается та, что лежит в среднем блоке
M = [1, p] × [(p+1)/2, (3p-1)/2] — остаётся 3(p-1) точек, никакие три не на прямой).
Живая клетка: не лежит ни на одной прямой через две точки множества (и не занята).
Рост: пока есть живые — добавить ту, что убивает меньше всех остальных живых (ничьи — случайно, seed).
Предсказание (записано до счёта, ledger строка 2 / сообщение 4d8ed50b): при p = 101 живых после семени < 20,
рост добавит ≤ 4. Ни одно из этих чисел не является целью или параметром поиска (independent_of_target).
usage: python3 candidate1_death_growth.py calibrate | run p [seeds]
"""
import sys, random
from math import gcd

def hjsw(p, c=1):
    h = (p - 1) // 2
    S = []
    for x in range(-h, 3 * h + 2):
        for y in range(0, 2 * p):
            if x % p and y % p and (x * y - c) % p == 0:
                if 1 <= x <= p and (p + 1) // 2 <= y <= (3 * p - 1) // 2:
                    continue                      # средний блок M — вычёркиваем
                S.append((x + h, y))              # сдвиг в сетку [0, 2p)²
    return S

def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) == 0

def brute_no_three(S):
    n = len(S)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if collinear(S[i], S[j], S[k]): return False
    return True

def dead_cells(S, n):
    """клетки, лежащие на прямой через две точки S (внутри сетки n×n), плюс сами точки S"""
    dead = set(S)
    m = len(S)
    for i in range(m):
        ax, ay = S[i]
        for j in range(i + 1, m):
            bx, by = S[j]
            dx, dy = bx - ax, by - ay
            g = gcd(abs(dx), abs(dy)); dx //= g; dy //= g
            x, y = ax, ay
            while 0 <= x < n and 0 <= y < n: dead.add((x, y)); x += dx; y += dy
            x, y = ax - dx, ay - dy
            while 0 <= x < n and 0 <= y < n: dead.add((x, y)); x -= dx; y -= dy
    return dead

def live_cells(S, n):
    dead = dead_cells(S, n)
    return [(x, y) for x in range(n) for y in range(n) if (x, y) not in dead]

def live_cells_brute(S, n):
    out = []
    for x in range(n):
        for y in range(n):
            if (x, y) in set(S): continue
            ok = True
            for i in range(len(S)):
                for j in range(i + 1, len(S)):
                    if collinear(S[i], S[j], (x, y)): ok = False; break
                if not ok: break
            if ok: out.append((x, y))
    return out

def kills(S, live, cand):
    """сколько живых клеток (кроме cand) умрёт, если добавить cand"""
    k = 0
    for q in live:
        if q == cand: continue
        for s in S:
            if collinear(s, cand, q): k += 1; break
    return k

def grow(S, n, seed=0):
    rng = random.Random(seed)
    S = list(S); live = live_cells(S, n); added = []
    while live:
        scored = [(kills(S, live, c), rng.random(), c) for c in live]
        scored.sort()
        c = scored[0][2]
        S.append(c); added.append(c)
        live = live_cells(S, n)
    return added

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "calibrate":
        for p in (5, 7, 11, 13):
            S = hjsw(p); n = 2 * p
            assert len(S) == 3 * (p - 1), (p, len(S))
            assert all(0 <= x < n and 0 <= y < n for x, y in S)
            assert brute_no_three(S), p
            print(f"p={p}: |HJSW|={len(S)}=3(p-1), no three collinear — OK")
        rng = random.Random(1)
        for t in range(5):
            n = rng.choice((8, 10, 12)); S = rng.sample([(x, y) for x in range(n) for y in range(n)], rng.choice((4, 6, 8)))
            a = sorted(live_cells(S, n)); b = sorted(live_cells_brute(S, n))
            assert a == b, (n, S)
            print(f"random n={n} |S|={len(S)}: live={len(a)} — линейный счётчик == перебор OK")
        print("calibration passed")
    else:
        p = int(sys.argv[2]); seeds = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        S = hjsw(p); n = 2 * p
        assert len(S) == 3 * (p - 1)
        live = live_cells(S, n)
        print(f"p={p} n={n}: |seed|={len(S)}, live cells after seed = {len(live)}")
        for sd in range(seeds):
            added = grow(S, n, seed=sd)
            final = S + added
            ok = brute_no_three(final) if len(final) <= 320 else 'skipped'
            print(f"  seed {sd}: added {len(added)} points -> {len(final)}; no-three check: {ok}")
            with open(f"cand1_p{p}_seed{sd}_{len(final)}pts.txt", "w") as f:
                f.write(f"# candidate 1 (vtora): HJSW seed p={p} c=1 in {n}x{n} + least-damage growth, seed {sd}; {len(final)} points; no-three: {ok}\n")
                f.write(f"# live after seed: {len(live)}; added (in order): {added}\n")
                for x, y in final: f.write(f"{x} {y}\n")
