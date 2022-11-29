import mill._, scalalib._
import java.nio.file.Paths

object chisel extends ScalaModule {
  def scalaVersion = "2.13.10"

  def millSourcePath = super.millSourcePath / os.up

  override def scalacOptions = Seq(
    "-language:reflectiveCalls",
    "-deprecation",
    "-feature",
    "-Xcheckinit",
    s"-Xplugin:${plugin_path().path}",
    "-P:chiselplugin:genBundleElements"
  )

  def unmanagedClasspath = T {
    val lib_path = T.ctx.env.get("MILL_LIB") match {
      case Some(lib) => os.Path(Paths.get(lib).toAbsolutePath)
      case None      => millSourcePath / "lib"
    }
    if (!os.exists(lib_path)) Agg()
    else Agg.from(os.list(lib_path).map(PathRef(_)))
  }

  def plugin_path = T {
    val path = T.ctx.env.get("MILL_PLUGIN") match {
      case Some(p) => os.Path(Paths.get(p).toAbsolutePath)
      case None      => millSourcePath / "plugin"
    }
    PathRef(path / "plugin.jar")
  }

  override def scalacPluginClasspath = T {
   super.scalacPluginClasspath() ++ Agg(
     plugin_path()
   )
  }

}
