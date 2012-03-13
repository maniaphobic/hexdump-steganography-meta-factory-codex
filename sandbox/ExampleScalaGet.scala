//
// From http://gregluck.com/blog/archives/2009/01/scala-example-for-accessing-ehcache-server/
//

import java.net.URL
import scala.io.Source.fromInputStream
object ExampleScalaGet extends App {
val url = new URL("http://maniaphobic.org/hexdump/13425")
fromInputStream(url.openStream).getLines.foreach(print)
}
