"""
The Gale-Shapley algorithm.
Given two sets of elements, each with a preference list of the other set,
find a stable matching between the two sets.

In each round:
- Unmatched group 1 members propose to their most preferred, unmatched group 2 member.
- Each group 2 member that receives any proposals will accept the proposal from their 
  most preferred group 1 member.
Continue until all members are matched.

Overall loop (# rounds) is upper + lower bounded on the number of group 1 members, Theta(n).  
Each iteration of the loop is bounded by the number of group 2 members (preferences list), O(n).
Overall time complexity is O(n^2).
"""

from typing import Hashable, TypeVar

MATCH_TYPE_ONE = TypeVar("MATCH_TYPE_ONE", bound=Hashable)
MATCH_TYPE_TWO = TypeVar("MATCH_TYPE_TWO", bound=Hashable)


def stable_match(
    pref_1: dict[MATCH_TYPE_ONE, list[MATCH_TYPE_TWO]],
    pref_2: dict[MATCH_TYPE_TWO, list[MATCH_TYPE_ONE]],
) -> list[tuple[MATCH_TYPE_ONE, MATCH_TYPE_TWO]]:

    # Deep copy Pref1
    g1_preference = {g1: pref_1[g1] for g1 in pref_1}

    # O(1) lookup for how a group2 index ranks a particular group1
    # {
    #   g2.0: {
    #       g1.0: 0,
    #       g1.1: 2,
    #       g1.2: 0
    #   }
    # }
    g2_scores = {g2: {g1: i for i, g1 in enumerate(pref_2[g2])} for g2 in pref_2}

    # Keep track of the groups that are still available
    remaining_group1 = set(pref_1.keys())
    remaining_group2 = set(pref_2.keys())

    # The final matchings
    matchings = []

    while remaining_group1:
        round_offers_to_g2 = dict()
        for g1 in remaining_group1:
            # Iterate over all remaining g1

            while g1_chooses := g1_preference[g1].pop(0):
                # Find the first available g2 that g1 has not offered to yet
                if g1_chooses in remaining_group2:
                    break

            g2_reciprocal_score = g2_scores[g1_chooses][g1]

            if g1_chooses not in round_offers_to_g2:
                # If this is the first offer this g2 has received this round
                # then no comparison is needed
                round_offers_to_g2[g1_chooses] = (g1, g2_reciprocal_score)

            elif g2_reciprocal_score < round_offers_to_g2[g1_chooses][1]:
                # If g2 prefers this offer over any previous offer
                # then replace the previous offer
                round_offers_to_g2[g1_chooses] = (g1, g2_reciprocal_score)

        # Maintain the acceptance invariants
        for g2, (g1, _) in round_offers_to_g2.items():
            remaining_group1.remove(g1)
            remaining_group2.remove(g2)
            matchings.append((g1, g2))

    return matchings


if __name__ == "__main__":

    l1 = {
        "A": [0, 1, 2],
        "B": [0, 2, 1],
        "C": [1, 2, 0],
    }
    l2 = {
        0: ["C", "B", "A"],
        1: ["A", "B", "C"],
        2: ["A", "C", "B"],
    }

    rez = stable_match(l1, l2)
    print(rez)
