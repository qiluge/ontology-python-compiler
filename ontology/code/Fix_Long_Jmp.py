def fix_all_vmtoken_addr(all_token, insertaddr):
    for addr, vmtoken in all_token:
        if addr >= insertaddr:
            addr += 1
    
def fix_all_label_addr(all_label, insertaddr):
    for label in range(len(all_label)):
        if all_label[label] >= insertaddr:
            all_label[label] += 1
 
def fix_long_jmp(oldjmptoken):
    if offset > 32767:
        bakend = True
        insertaddr = oldjmptoken.addr + 32767
    elif offset < -32767:
        bakend = False
        insertaddr = oldjmptoken.addr - 32767
        assert(insertaddr >= 0)
   
    # assert new jmp label
    newjmplabel = newlabel()
    newjmplabel.addr = insertaddr
    
    # assert new jmp offset
    newjmptoken.data = oldjmptoken.label
    if bakend:
        assert(insertaddr < oldjmptoken.label.addr)
    elif not bakend:
        assert(insertaddr > oldjmptoken.label.addr)
    
    # assert old jmp offset
    oldjmptoken.data = newjmplabel
    
    # insert
    insert_token_at_addr(jmpoken, addr)
    
    newoffset = insertaddr - newjmptoken.data.addr
    if newoffset > 32767:
        fix_long_jmp(newjmptoken)
    elif newoffset < -32767:
        fix_long_jmp(newjmptoken)

    return
