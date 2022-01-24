def calc_gc_content(seq):
    if len(seq) ==0:
        return 0.0
    gc_content=(seq.upper().count("C")+ seq.upper().count("G")) / len(seq)*100
    return gc_content
