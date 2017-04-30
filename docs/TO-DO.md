# TODO

* Function semantics
* * pass correct no. of args, check return type
* * test with global vars, then with functions

* Free up var table at end of procedure
* VM

* CREATE AUTOMATED TESTS, TO RUN EVERYTIME WE DO CHANGE

* Translate addresses from vars to virtual addresses in quads
    * Divide global / globaltemp / local / localtemp /const vars and their types
    * Option 1 : parser - mem_controller - parser - quad_controller
    * Option 2 : parser - quad_controller - mem_controller - quad_controller

* Save local and temp memory counters to corresponding function when finishing function
* Restart counters for local and temp memory everytime we enter a new function