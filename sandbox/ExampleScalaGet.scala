//
// From http://gregluck.com/blog/archives/2009/01/scala-example-for-accessing-ehcache-server/
//

import java.net.URL
import scala.io.Source.fromInputStream
object ExampleScalaGet {
  def main (args: Array[String]) {
    args.foreach { arg =>
      val url = new URL(arg)
      fromInputStream(url.openStream).getLines.foreach(print)
    }
  }
}
