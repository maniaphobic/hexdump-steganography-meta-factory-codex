object PhaseTwo {

    val fragments = List(
        "TOP SECRET",
        "",
        "FROM: Special Operations Division, Army Biological Warfare Laboratories, Camp Detrick, Frederick, MD",
        "TO:   Commander, Office of Advanced Weapons, Chemical Warfare Service",
        "DATE: 10 July 1943",
        "",
        "",
        "",
        "",
        ""
    )

    def main(args: Array[String]) {
    	val delay = new scala.util.Random
    	for (fragment: String <- fragments) {
	    for (letter: Char <- fragment) {
	        print(letter)
		Thread sleep (delay nextInt(100) + 0)
            }
	    println("")
	}
    }
}
