def combine(listable, built = [], listed = []):
    if len(listable) <= 0:
        if len(built) > 0:
            listed.append(built + [])
        return

    combine(listable[1:], built, listed)
    combine(listable[1:], built + [listable[0]], listed)

    return listed