import mill._, scalalib._
import java.nio.file.Paths

object knitkit extends ScalaModule {
  def scalaVersion = "2.13.6"

  def millSourcePath = super.millSourcePath / os.up

  def unmanagedClasspath = T {
    val lib_path = T.ctx.env.get("MILL_LIB") match {
      case Some(lib) => os.Path(Paths.get(lib).toAbsolutePath)
      case None      => millSourcePath / "lib"
    }
    if (!os.exists(lib_path)) Agg()
    else Agg.from(os.list(lib_path).map(PathRef(_)))
  }
}
