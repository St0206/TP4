def tri_selection(tab):
    n=len(tab)
    for i in range (n):
        min_index=i
        for j in range (i+1,n):
            if tab[j]<tab[i]:
                min_index=j
        if min_index != i:
            tab[i],tab[min_index]= tab[min_index],tab[i]
        print(f"Etape {i+1}: {tab}")
    return tab

tab = [15, 2, 4, 8, 1, 31]
print("Liste originale :", tab)
print("\nÉvolution du tri :")
tri_selection(tab.copy())
print("\nUtilisation de sorted() :")
sorted_tab = sorted(tab)
print("Résultat avec sorted():", sorted_tab)
print("Liste tab après sorted():",sorted_tab)
print("\nUtilisation de sort() :")
tab.sort()
print("Liste tab après sort():", tab)




