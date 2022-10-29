def dicoDjikstra(dico,s,fin):

    infini = sum(sum(dico[s1][s2] for s2 in dico[s1]) for s1 in dico) + 1
    s_connu = {s:[0,[s]]}
    s_inconnu = {k:[infini,''] for k in dico if k!=s}
    for suivant in dico[s]:
        s_inconnu[suivant] = [dico[s][suivant],s]

    while s_inconnu and any(s_inconnu[k][0] < infini for k in s_inconnu):
        u=min(s_inconnu, key=s_inconnu.get)
        longueur_u,precedent_u=s_inconnu[u]

        for v in dico[u]:
            if v in s_inconnu:
                d= longueur_u + dico[u][v]
                if d<s_inconnu[v][0]:
                    s_inconnu[v]=[d,u]


        s_connu[u]=[longueur_u, s_connu[precedent_u][1]+[u]]

        del s_inconnu[u]


    for key in s_connu.keys():
        if key == fin:
            return s_connu[key]
