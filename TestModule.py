# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:39:05 2016

@author: tanfan.zjh
"""

from structure import DependencyTree as tree
import DepNN as nn
from execute import Execute as exe

lines = ('[(S (NP (DT Those) (NN space)) (VP (VBZ walks) (SBAR (S (VP (VBP are) (S (VP (TO to) (VP (VB be) (VP (VBN used) (PP (IN for) (S (VP (VBG preparing) (NP (NP (DT the) (NNP ISS)) (PP (IN for) (NP (NP (DT the) (VBN planned) (NN docking)) (NP (JJ next) (NN year)) (PP (IN of) (NP (DT the) (JJ new) (NNP European) (NNP ATV) (NN space) (NN cargo) (NN vessel))))))))))))))))) (. .))]','[det(space-2, Those-1), nsubj(walks-3, space-2), root(ROOT-0, walks-3), ccomp(walks-3, are-4), aux(used-7, to-5), auxpass(used-7, be-6), xcomp(are-4, used-7), prepc_for(used-7,preparing-9), det(ISS-11, the-10), dobj(preparing-9, ISS-11), det(docking-15, the-13), amod(docking-15, planned-14), prep_for(ISS-11, docking-15), amod(year-17, next-16), dep(docking-15, year-17), det(vessel-25, the-19), amod(vessel-25, new-20), nn(vessel-25, European-21), nn(vessel-25, ATV-22), nn(vessel-25, space-23), nn(vessel-25, cargo-24), prep_of(docking-15, vessel-25)]')
exe.train_sentence(lines[1])
    
