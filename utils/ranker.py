def rank_candidates(candidates):

    ranked = sorted(
        candidates,
        key=lambda x: x["score"]["final_score"],
        reverse=True
    )

    return ranked