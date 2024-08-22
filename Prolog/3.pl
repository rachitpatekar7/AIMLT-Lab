bigger(elephant,horse).
bigger(horse,donkey).
bigger(donkey,dog).
bigger(donkey,monkey).

bigger(X,Y):- bigger(X,Z),bigger(Z,Y).

