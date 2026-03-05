% Master Loader for ATM Expert Knowledge Base
% Point the Inference Engine to this file to load both facts and rules.

:- consult('atm_kb.pl'). % The generated facts
:- consult('rules.pl').  % The diagnostic logic
