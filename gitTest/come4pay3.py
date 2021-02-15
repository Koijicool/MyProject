def comeXpayY(come_x, pay_y, per_head, pax):
    """
   
    :param come_x: 
    :param pay_y: 
    :param per_head: 
    :param pax: 
    :return: 
    """
    return (pax // come_x) * (pay_y * per_head) + (pax % come_x) * per_head

if __name__ == '__main__':
    print(comeXpayY(4, 3, 100, 5))

