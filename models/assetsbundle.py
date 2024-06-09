from odoo.addons.base.models.assetsbundle import AssetsBundle, JavascriptAsset, CompileError
from subprocess import Popen, PIPE
import subprocess
from odoo.tools import misc

def transpile_jsx(content_bundle):
    npm_root = subprocess.run(['npm', '-g', 'root'], text=True, capture_output=True)
    command = ['babel', '--presets', npm_root.stdout + '/@babel/preset-react', '--no-babelrc']
    try:
        compiler = Popen(command, stdin=PIPE, stdout=PIPE,
                         stderr=PIPE)
    except Exception:
        raise CompileError("Could not execute command %r" % command[0])
    (out, err) = compiler.communicate(input=content_bundle)
    if compiler.returncode:
        cmd_output = misc.ustr(out) + misc.ustr(err)
        if not cmd_output:
            cmd_output = u"Process exited with return code %d\n" % compiler.returncode
        raise CompileError(cmd_output)
    return out

    
class JsxAsset(JavascriptAsset):
    @property
    def content(self):
        print('jsx asset content')
        content = super().content
        content = transpile_jsx(content.encode('utf-8')).decode('utf-8')
        #print (content)
        return content

class AssetsBundleJsx(AssetsBundle):
    def __init__(self, bundle_name, files, external_assets, env, css=True, js=True, debug_assets=False, rtl=False, assets_params=None):
        super(AssetsBundleJsx, self).__init__(bundle_name, files, external_assets, env=env, css=css, js=js, debug_assets=debug_assets, rtl=rtl, assets_params=assets_params)

        for idx, js in enumerate(self.javascripts):
            if js._filename and js._filename.find('react') >= 0:
                print(js._filename)
                self.javascripts[idx] = JsxAsset(self, url=js.url, filename=js._filename, inline=js.inline)

    def js(self):
        """
        Override the base implementation to 
        run transpiler on js content, and re-save attachment.
        note that transpiler always run on the bundle
        This is a POC, and not intended for production.
        Further optimization needed 
        """ 
        ira = super().js()
        return ira
