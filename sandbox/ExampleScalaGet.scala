//
// From http://gregluck.com/blog/archives/2009/01/scala-example-for-accessing-ehcache-server/
//

import java.net.URL
import scala.io.Source.fromInputStream
object ExampleScalaGet {
  def main (args: Array[String]) {
    val url = new URL(args(1))
    fromInputStream(url.openStream).getLines.foreach(print)
  }
}
