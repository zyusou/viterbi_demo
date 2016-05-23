# ソースはこのページにあり，このページのソースコードを改変しています．
# http://yuutookun.hatenablog.com/entry/2012/10/07/153101

# 状態集合Q（HMMで言う品詞の集合）
states = ("rainy", "sunny")

# 観測したシーケンスO（HMMで言う，入力単語列）
observations = ("walk", "shop", "clean", "shop", "walk")

# 初期状態の事前確率
start_prob = {"rainy": 0.6, "sunny": 0.4}

# 状態遷移確率A（タグからタグへの遷移確率）
transit_prob = {"rainy": {"rainy": 0.7, "sunny": 0.3},
                "sunny": {"rainy": 0.4, "sunny": 0.6}}

# 尤度B（タグからその単語が出る確率）
emission_prob = {'rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
                 'sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1}}


def viterbi(observs, states, sp, tp, ep):
    """viterbi algorithm
    Output : labels estimated"""
    T = {}  # present state
    for st in states:
        T[st] = (sp[st] * ep[st][observs[0]], [st])
    for ob in observs[1:]:
        T = next_state(ob, states, T, tp, ep)
    prob, labels = max([T[st] for st in T])
    return prob, labels


def next_state(ob, states, T, tp, ep):
    """calculate a next state's probability, and get a next path"""
    U = {}  # next state
    for next_s in states:
        U[next_s] = (0, [])
        for now_s in states:
            p = T[now_s][0] * tp[now_s][next_s] * ep[next_s][ob]
            if p > U[next_s][0]:
                U[next_s] = [p, T[now_s][1] + [next_s]]
    return U


if __name__ == "__main__":
    print(observations)
    a, b = viterbi(observations, states,
                   start_prob, transit_prob, emission_prob)
    print(b)
    print(a)
