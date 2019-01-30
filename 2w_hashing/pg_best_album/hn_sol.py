def solution(genres, plays):
    dict = {}
    answer = []
    for i, genre in enumerate(genres):
        try:
            if dict[genre]==None:pass
            dict[genre].append((i,plays[i]))
        except KeyError:
            dict[genre] = [(i,plays[i])]
    sortedByGenres = sorted(dict.items(), key=lambda k:sum([play for it, play in k[1]]), reverse=True)
    for genre, plays in sortedByGenres:
        plays = sorted(plays, key=lambda play:play[1], reverse=True)
        # 이부분은 heapq의 nlargest? 그걸로 가능할 듯
        answer += [i for i, play in plays[:2]]
    return answer

genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
answer = solution(genres, plays)
print(answer)
