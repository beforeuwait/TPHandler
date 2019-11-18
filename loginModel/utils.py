# coding=utf-8


# cookie编辑
def cookie_transform(c_l):
    return {"Cookie": ';'.join(['='.join([c[0], str(c[1])])for c in c_l])}

