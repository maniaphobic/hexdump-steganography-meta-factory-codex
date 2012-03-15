//
// From http://gregluck.com/blog/archives/2009/01/scala-example-for-accessing-ehcache-server/
//

import java.net.URL
import scala.io.Source.fromInputStream

object PhaseTwo {

  val key = 'abcde'
  val plaintext = '1234567980'

  def main (args: Array[String]) {

    

    args.foreach { arg =>
      val url = new URL(arg)
      try {
        fromInputStream(url.openStream).getLines.foreach(print)
      } catch {
        case e: java.net.UnknownHostException => println("Unknown host: " + arg)
        case e: java.io.FileNotFoundException => println("Unknown file: " + arg)
        case e: Exception => println("Unknown exception caught: " + e)
      }
    }
  }
}
