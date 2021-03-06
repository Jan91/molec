import math
import numpy as np
import pandas as pd

import matplotlib as plt
import matplotlib.pyplot as pyplot
from pylab import *

import seaborn as sns

def sns_pair_plot(target, var_list, file, redshift):

	sns.set_style("white")
	sns.set_style("ticks")
	sns.set_context("talk")

	data = pd.read_pickle(file)
	
	plt.figure()

	data_f = {}

	for var in var_list:
		if var in ['NTOTH2', 'TEMP', 'B']:
			data_f[var] = data[var][0]
		if var == 'A_Z':
			data_f[var] = data[var][0]/100000.0 + redshift

	df = pd.DataFrame(data_f)

	g = sns.PairGrid(df) #, diag_kws=dict(color="blue", shade=True))
	g.map_upper(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_lower(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_diag(plt.hist) #, lw=2);
	
	#g.axes[0,0].set_ylim(redshift-0.0002,redshift+0.00005)
	g.axes[0,0].set_ylabel(r"$z$")
	g.axes[1,0].set_ylabel(r"$b$")
	g.axes[2,0].set_ylabel(r"$N(H_2)$")
	#g.axes[3,0].set_ylabel(r"$N(HI)$")
	g.axes[3,0].set_ylabel(r"$T$")

	#g.axes[3,0].set_xlim(redshift-0.0002,redshift+0.00005)
	g.axes[3,0].set_xlabel(r"$z$")
	g.axes[3,1].set_xlabel(r"$b$")
	g.axes[3,2].set_xlabel(r"$N(H_2)$")
	#g.axes[4,3].set_xlabel(r"$N(HI)$")
	g.axes[3,3].set_xlabel(r"$T$")

	g.savefig(target + "H2_pairplot.pdf")

def sns_H2s_pair_plot(target, var_list, file, redshift):

	sns.set_style("white")
	sns.set_style("ticks")
	sns.set_context("talk")

	data = pd.read_pickle(file)
	
	plt.figure()

	data_f = {}

	for var in var_list:
		if var in ['NH2', 'B']:
			data_f[var] = data[var][0]
		if var == 'A_Z':
			data_f[var] = data[var][0]/100000.0 + redshift

	df = pd.DataFrame(data_f)

	g = sns.PairGrid(df) #, diag_kws=dict(color="blue", shade=True))
	g.map_upper(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_lower(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_diag(plt.hist) #, lw=2);
	
	g.axes[0,0].set_ylabel(r"$z$")
	g.axes[1,0].set_ylabel(r"$b$")
	g.axes[2,0].set_ylabel(r"$N(H_2)$")

	g.axes[2,0].set_xlabel(r"$z$")
	g.axes[2,1].set_xlabel(r"$b$")
	g.axes[2,2].set_xlabel(r"$N(H_2)$")

	g.savefig(target + "H2s_pairplot.pdf")

def sns_H2all_pair_plot(target, var_list, file, redshift):

	sns.set_style("white")
	sns.set_style("ticks")
	sns.set_context("talk")

	data = pd.read_pickle(file)
	
	plt.figure()

	data_f = {}

	for var in var_list:
		if var == 'B':
			data_f[var] = data[var][0]
		if var == 'A_Z':
			data_f[var] = data[var][0]/100000.0 + redshift
		if var.startswith('NH'):
			data_f[var] = data[var][0]

	df = pd.DataFrame(data_f)

	g = sns.PairGrid(df) #, diag_kws=dict(color="blue", shade=True))
	g.map_upper(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_lower(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_diag(plt.hist) #, lw=2);
	
	g.axes[0,0].set_ylabel(r"$z$")
	g.axes[1,0].set_ylabel(r"$b$")
	#g.axes[2,0].set_ylabel(r"$N(H_2)$")

	g.axes[2,0].set_xlabel(r"$z$")
	g.axes[2,1].set_xlabel(r"$b$")
	#g.axes[2,2].set_xlabel(r"$N(H_2)$")

	g.savefig(target + "H2all_pairplot.pdf")


def sns_pair_plot_fb(target, var_list, file, redshift, fb):
	'''
	pair plot for fixed broadening parameter
	'''

	sns.set_style("white")
	sns.set_style("ticks")
	sns.set_context("talk")

	data = pd.read_pickle(file)
	
	plt.figure()

	data_f = {}

	for var in var_list:
		if var in ['NTOTH2', 'TEMP']:
			data_f[var] = data[var][0]
		if var == 'A_Z':
			data_f[var] = data[var][0]/100000.0 + redshift

	df = pd.DataFrame(data_f)

	g = sns.PairGrid(df) #, diag_kws=dict(color="blue", shade=True))
	g.map_upper(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_lower(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_diag(plt.hist) #, lw=2);
	
	#g.axes[0,0].set_ylim(redshift-0.0002,redshift+0.00005)
	g.axes[0,0].set_ylabel(r"$z$")
	g.axes[1,0].set_ylabel(r"$N(H_2)$")
	#g.axes[2,0].set_ylabel(r"$N(HI)$")
	g.axes[2,0].set_ylabel(r"$T$")

	#g.axes[3,0].set_xlim(redshift-0.0002,redshift+0.00005)
	g.axes[2,0].set_xlabel(r"$z$")
	g.axes[2,1].set_xlabel(r"$N(H_2)$")
	#g.axes[3,2].set_xlabel(r"$N(HI)$")
	g.axes[2,2].set_xlabel(r"$T$")

	g.savefig(target+"_b_"+str(fb)+"_H2_pairplot.pdf")

def sns_pair_plot_CO(target, var_list, file, redshift):

	sns.set_style("white")
	sns.set_style("ticks")
	sns.set_context("talk")

	data = pd.read_pickle(file)
	
	plt.figure()

	data_f = {}

	for var in var_list:
		if var in ['NTOTCO', 'TEMP', 'B']:
			data_f[var] = data[var][0]
		if var == 'A_Z':
			data_f[var] = data[var][0]/100000.0 + redshift

	df = pd.DataFrame(data_f)

	g = sns.PairGrid(df) #, diag_kws=dict(color="blue", shade=True))
	g.map_upper(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_lower(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_diag(plt.hist) #, lw=2);
	
	#g.axes[0,0].set_ylim(redshift-0.0002,redshift+0.00005)
	g.axes[0,0].set_ylabel(r"$z$")
	g.axes[1,0].set_ylabel(r"$b$")
	g.axes[2,0].set_ylabel(r"$N(CO)$")
	g.axes[3,0].set_ylabel(r"$T$")

	#g.axes[3,0].set_xlim(redshift-0.0002,redshift+0.00005)
	g.axes[3,0].set_xlabel(r"$z$")
	g.axes[3,1].set_xlabel(r"$b$")
	g.axes[3,2].set_xlabel(r"$N(CO)$")
	g.axes[3,3].set_xlabel(r"$T$")

	g.savefig(target + "CO_pairplot.pdf")

def sns_pair_plot_CO_fb(target, var_list, file, redshift, fb):

	sns.set_style("white")
	sns.set_style("ticks")
	sns.set_context("talk")

	data = pd.read_pickle(file)
	
	plt.figure()

	data_f = {}

	for var in var_list:
		if var in ['NTOTCO', 'TEMP']:
			data_f[var] = data[var][0]
		if var == 'A_Z':
			data_f[var] = data[var][0]/100000.0 + redshift

	df = pd.DataFrame(data_f)

	g = sns.PairGrid(df) #, diag_kws=dict(color="blue", shade=True))
	g.map_upper(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_lower(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_diag(plt.hist) #, lw=2);
	
	#g.axes[0,0].set_ylim(redshift-0.0002,redshift+0.00005)
	g.axes[0,0].set_ylabel(r"$z$")
	g.axes[1,0].set_ylabel(r"$N(CO)$")
	g.axes[2,0].set_ylabel(r"$T$")

	#g.axes[3,0].set_xlim(redshift-0.0002,redshift+0.00005)
	g.axes[2,0].set_xlabel(r"$z$")
	g.axes[2,1].set_xlabel(r"$N(CO)$")
	g.axes[2,2].set_xlabel(r"$T$")

	g.savefig(target+"_b_"+str(fb)+"_CO_pairplot.pdf")


def sns_velo_pair_plot(target, line, file, nvoigts):

	sns.set_style("white")
	sns.set_style("ticks")
	sns.set_context("talk")


	for i in np.arange(1, nvoigts + 1, 1):

		data = pd.read_pickle(file)
		plt.figure()

		data_f = {}

		for key in data:
			if key.startswith(("v0", "N", "b")) and key.endswith(str(i)):
				data_f[key] = data[key][0]
			if key in ["a", "a1", "a2"]:
				data_f[key] = data[key][0]
		
		df = pd.DataFrame(data_f)
		#g = sns.pairplot(df, diag_kind="kde")

		g = sns.PairGrid(df) #, diag_kws=dict(color="blue", shade=True))
		g.map_upper(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
			shade_lowest=False)
		g.map_lower(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
			shade_lowest=False)
		#g.map_diag(sns.kdeplot, lw=2);
		g.map_diag(plt.hist)
		g.savefig(target+"_"+str(nvoigts)+"_"+str(i)+"_"+str(line)+"_"+"v.pdf")

def sns_H2vib_plot(target, var_list, file, redshift):

	var_list = var_list

	data = pd.read_pickle(file)
	
	plt.figure()

	data_f = {}

	for var in var_list:
		if not var.startswith(("B_", "A_")):
			data_f[var] = data[var][0]
		if var == "A_Z":
			data_f[var] = data[var][0]/100000.0 + redshift

	df = pd.DataFrame(data_f)
	#g = sns.pairplot(df)

	g = sns.PairGrid(df)
	g.map_upper(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_lower(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_diag(plt.hist)

	g.axes[0,0].set_ylabel(r"$z$")
	g.axes[2,0].set_ylabel(r"$z$")

	g.savefig(target + "H2vib_pairplot.pdf")



def sns_velo_trace_plot(target, line, file, nvoigts):

	sns.set(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
	pal = sns.cubehelix_palette(4, rot=-.25, light=.7)

	for i in np.arange(1, nvoigts + 1, 1):

		data = pd.read_pickle(file)

		f, axes = plt.subplots(4, 1, figsize=(10, 6), sharex=True)

		data_f = {}

		for key in data:
			if key.endswith(str(i)):
				data_f[key] = data[key][0]
			if key == "a":
				data_f[key] = data[key][0]
		
		x = np.arange(0, len(data_f['N'+str(i)]), 1)

		df = pd.DataFrame(data_f)

		axes[0].plot(x, df['a'],color=pal[0])
		axes[1].plot(x, df['N'+str(i)],color=pal[1])
		axes[2].plot(x, df['b'+str(i)],color=pal[2])
		axes[3].plot(x, df['v0'+str(i)],color=pal[3])

		#axes[1].set_ylim([0, 24])
		#axes[2].set_ylim([0, 30])

		axes[0].set_ylabel('a')
		axes[1].set_ylabel('N'+str(i))
		axes[2].set_ylabel('b'+str(i))
		axes[3].set_ylabel('v0'+str(i))	
		axes[3].set_xlabel("Iterations")	

		f.savefig(target+"_"+str(nvoigts)+"_"+str(i)+"_"+str(line)+"_"+"trace_plot.pdf")


def plot_H2fit_elmt(target, element, file):

	var_list = ["N_"+element,"B_"+element]
	data = pd.read_pickle(file)
	plt.figure()

	data_f = {}

	for key in data:
		if key.startswith('N_NV') or key.startswith('B_NV'):
			print key 
			data_f[key] = data[key][0]

	df = pd.DataFrame(data_f)

	g = sns.PairGrid(df)
	g.map_upper(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_lower(sns.kdeplot, cmap="bone_r",n_levels=10,shade=True,
		shade_lowest=False)
	g.map_diag(plt.hist)
	g.savefig(target+"_"+str(element)+"_pair_plot.pdf")










